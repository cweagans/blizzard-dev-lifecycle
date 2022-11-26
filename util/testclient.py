import http.client
import json
import sys
import time


def main():
    starttime = time.time()
    total_reqs = 0
    non_200_reqs = 0
    last_version = ""

    try:
        while True:
            connection = http.client.HTTPConnection('translationapi.localtest.me', 80, timeout=10)
            connection.request("GET", "/version")
            response = connection.getresponse()
            total_reqs += 1
            if total_reqs % 1000 == 0:
                print(f"{total_reqs} sent. {non_200_reqs} failures.")

            if response.status != 200:
                non_200_reqs += 1
                print("New failed request.")
            else:
                res_text = response.read().decode()
                data = json.loads(res_text)
                if data["version"] != last_version:
                    last_version = data["version"]
                    print(f"{total_reqs} sent. {non_200_reqs} failures.")
                    print(f"New version found: {last_version}")

    except KeyboardInterrupt:
        endtime = time.time()
        totaltime = round(endtime - starttime, 2)
        rps = round(total_reqs/totaltime, 2)
        print("\n\nSummary:\n")
        print(f"Total requests:      {total_reqs}")
        print(f"Failed requests:     {non_200_reqs}")
        print(f"Total run time:      {totaltime}s")
        print(f"Requests per second: {rps}")
        print(f"Most recent version: {last_version}")
        sys.exit()


if __name__ == '__main__':
    main()

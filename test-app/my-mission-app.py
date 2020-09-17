#!/usr/bin/env python3

import argparse
import app_api

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', '-c')
    args = parser.parse_args()
    if args.config is not None:
        SERVICES = app_api.Services(args.config)
    else:
        SERVICES = app_api.services()
    request = '{ ping }'
    response = SERVICES.query(service="monitor-service", query=request)
    data = response["ping"]
    if data == "pong":
        print("Successfully pinged monitor service")
    else:
        print("Unexpected monitor service response: %s" % data)

if __name__ == "__main__":
    main()
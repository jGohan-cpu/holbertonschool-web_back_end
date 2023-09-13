#!/usr/bin/env python3
"""Script that provides some stats about Ngix
logs stored in MongoDB"""
import pymongo


def print_stats(collection):
    # Get the total number of logs in the collection
    total_logs = collection.count_documents({})

    # Initialize counters for each HTTP method
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: 0 for method in http_methods}

    # Initialize a counter for status check
    status_check_count = 0

    # Iterate through the documents and count occurrences
    for log in collection.find():
        method = log.get("method")
        path = log.get("path")

        if method in method_counts:
            method_counts[method] += 1

        if method == "GET" and path == "/status":
            status_check_count += 1

    # Print the statistics
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"    method {method}:", count)
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    # Connect to the MongoDB server and select the "logs" database
    # and "nginx" collection
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
    collection = db["nginx"]

    # Calculate and print the statistics
    print_stats(collection)

    # Close the MongoDB connection
    client.close()

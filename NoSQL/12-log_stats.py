#!/usr/bin/env python3

""" provides some stats about Nginx logs stored in MongoDB """
import pymongo


def print_stats(collection):
    """
    Calculate and print statistics about Nginx logs.

    Args:
        collection (pymongo.collection.Collection): The MongoDB collection 
        containing Nginx logs.
    """
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


def get_nginx_logs_statistics():
    """Retrieves and displays statistics about Nginx 
    logs stored in MongoDB"""
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    db = client["logs"]
    collection = db["nginx"]

    total_logs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}

    for method in methods:
        method_count = collection.count_documents({"method": method})
        method_counts[method] = method_count

    status_logs = collection.count_documents({"method": "GET", "path":
                                              "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\t{count} {method}")
    print(f"{status_logs} logs with method=GET and path=/status")

    client.close()

    if __name__ == "__main__":
        get_nginx_logs_statistics()

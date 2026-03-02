server = {"dev": "safe to deploy", "staging": "safe to deploy", "prod": "need to be cautious"}
for s, note in server.items():
    print(f"{s} - {note}")
        
def pod_status(pod):
    for p in pod:
        if p['status'] == 'running':
            print(f"Pod {p['name']} is running.")
        elif p['status'] == 'pending':
            print(f"Pod {p['name']} is pending.")

pod = [{"name":"nginx","status":"running"},{"name":"apache","status":"pending"}]
pod_status(pod)

        
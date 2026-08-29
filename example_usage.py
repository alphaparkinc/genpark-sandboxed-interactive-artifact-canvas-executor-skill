from client import SandboxedInteractiveArtifactCanvasExecutorClient

def main():
    client = SandboxedInteractiveArtifactCanvasExecutorClient()
    res = client.execute_artifact_component('function Chart() { return React.createElement("svg", {width: 400, height: 200}); }')
    print('Artifact Canvas: ' + res['execution_session_id'] + ' (Runtime: ' + res['runtime'] + ')')
    print('Compiled: ' + str(res['compilation_successful']) + ' | Mounted: ' + str(res['sandboxed_dom_mounted']))
    print('Render Latency: ' + str(res['render_latency_ms']) + 'ms')
    print('Preview URL: ' + res['iframe_sandbox_preview_url'])

if __name__ == '__main__':
    main()

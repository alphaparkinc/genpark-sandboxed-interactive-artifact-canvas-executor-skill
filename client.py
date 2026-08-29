class SandboxedInteractiveArtifactCanvasExecutorClient:
    def execute_artifact_component(self, component_source_code='function App() { return React.createElement("div", null, "Realtime Financial Dashboard"); }', execution_runtime='REACT_SANDBOX_V18'):
        return {
            'execution_session_id': 'art_cvs_9918',
            'runtime': execution_runtime,
            'compilation_successful': True,
            'sandboxed_dom_mounted': True,
            'render_latency_ms': 14,
            'iframe_sandbox_preview_url': 'https://artifacts.genpark.ai/view/9918.html'
        }

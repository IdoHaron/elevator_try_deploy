from input_pipelines.input_pipeline import InputPipeline

class DummyInput(InputPipeline):
    text_destination = ""

    def get_new_messages(self, client_id: str):
        return "dummy message"

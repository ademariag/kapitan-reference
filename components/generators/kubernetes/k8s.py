from typing import Optional
from kapitan.inputs.kadet import BaseModel, BaseObj


class Base(BaseObj):
    def new(self):
        self.need("apiVersion")
        self.need("kind")
        self.need("name")

    def body(self):
        self.root.apiVersion = self.kwargs.apiVersion
        self.root.kind = self.kwargs.kind
        self.name = self.kwargs.name
        self.root.metadata.name = self.kwargs.get("rendered_name", self.name)
        self.add_label("name", self.root.metadata.name)

    def add_labels(self, labels):
        for key, value in labels.items():
            self.add_label(key, value)

    def add_label(self, key, value):
        self.root.metadata.labels[key] = value

    def add_namespace(self, namespace):
        self.root.metadata.namespace = namespace

    def add_annotations(self, annotations):
        for key, value in annotations.items():
            self.add_annotation(key, value)

    def add_annotation(self, key, value):
        self.root.metadata.annotations[key] = value


class BaseResource(BaseModel):
    apiVersion: str
    kind: str
    name: str
    rendered_name: Optional[str] = None

    def body(self):
        self.root.apiVersion = self.apiVersion
        self.root.kind = self.kind
        if self.rendered_name is None:
            self.rendered_name = self.name
        
        self.root.metadata.name = self.rendered_name
        self.add_label("name", self.rendered_name)

    def add_labels(self, labels):
        for key, value in labels.items():
            self.add_label(key, value)

    def add_label(self, key, value):
        self.root.metadata.labels[key] = value

    def add_namespace(self, namespace):
        self.root.metadata.namespace = namespace

    def add_annotations(self, annotations):
        for key, value in annotations.items():
            self.add_annotation(key, value)

    def add_annotation(self, key, value):
        self.root.metadata.annotations[key] = value

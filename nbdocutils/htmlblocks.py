from abc import ABC, abstractmethod


class HTMLBlock(ABC):
    """
    Base class for all html blocks. Has html property.
    """
    @property
    def html(self):
        from IPython.display import HTML
        return HTML(self.__str__())


class _AlertBlock(HTMLBlock, ABC):
    """
    Base class for alert blocks. Subclasses will specify value for {style} in __str__ method.
    """
    # TODO: Use template files.
    def __init__(self, style):
        self._format_string = """
        <div class="alert alert-block {style}">
            <b>{lead_in}:</b> {text}
        </div>
        """
        self.style = style

    @abstractmethod
    def __str__(self):
        # return self._format_string.format(style=self.style)
        pass
    

class BlueAlertBlock(_AlertBlock):
    """
    Class for inserting a blue alert-block.
    """
    def __init__(self, lead_in, text):
        super().__init__(style="alert-info")
        self.lead_in = lead_in
        self.text = text

    def __str__(self):
        return self._format_string.format(
            style=self.style,
            lead_in=self.lead_in,
            text=self.text
        )
from markitdown import MarkItDown, StreamInfo
from io import BytesIO
from pathlib import Path
from pydantic import Field


def binary_document_to_markdown(binary_data: bytes, file_type: str) -> str:
    """Converts binary document data to markdown-formatted text."""
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content


def document_path_to_markdown(
    file_path: str = Field(description="Absolute or relative path to a .pdf or .docx file"),
) -> str:
    """Convert a PDF or DOCX file on disk to markdown-formatted text.

    Reads the file at the given path, detects its format from the extension,
    and returns the full document content as markdown.

    When to use:
    - When you have a local file path to a PDF or DOCX document to extract text from

    When not to use:
    - When you already have the file contents as bytes — use binary_document_to_markdown instead
    - For file formats other than .pdf and .docx

    Examples:
    >>> document_path_to_markdown("/tmp/report.pdf")
    "# Report Title\\n\\nSome content..."
    >>> document_path_to_markdown("/tmp/notes.docx")
    "# Notes\\n\\n- Item one..."
    """
    path = Path(file_path)
    return binary_document_to_markdown(path.read_bytes(), path.suffix.lstrip("."))

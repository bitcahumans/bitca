from dataclasses import dataclass, field
from typing import Any, List

from bitca.document.base import Document
from bitca.document.chunking.fixed import FixedSizeChunking
from bitca.document.chunking.strategy import ChunkingStrategy


@dataclass
class Reader:
    """Base class for reading documents"""

    chunk: bool = True
    chunk_size: int = 3000
    separators: List[str] = field(default_factory=lambda: ["\n", "\n\n", "\r", "\r\n", "\n\r", "\t", " ", "  "])
    chunking_strategy: ChunkingStrategy = field(default_factory=FixedSizeChunking)

    def read(self, obj: Any) -> List[Document]:
        raise NotImplementedError

    def chunk_document(self, document: Document) -> List[Document]:
        return self.chunking_strategy.chunk(document)

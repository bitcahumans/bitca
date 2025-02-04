from typing import Iterator, List

from bitca.document import Document
from bitca.document.reader.csv_reader import CSVUrlReader
from bitca.knowledge.agent import AgentKnowledge
from bitca.utils.log import logger


class CSVUrlKnowledgeBase(AgentKnowledge):
    urls: List[str]
    reader: CSVUrlReader = CSVUrlReader()

    @property
    def document_lists(self) -> Iterator[List[Document]]:
        for url in self.urls:
            if url.endswith(".csv"):
                yield self.reader.read(url=url)
            else:
                logger.error(f"Unsupported URL: {url}")

"""`eds.leukemia` pipeline"""
from typing import Any, Dict, List, Optional, Union

from edsnlp.core import PipelineProtocol
from edsnlp.pipelines.base import SpanSetterArg

from ..base import DisorderMatcher
from .patterns import default_patterns


class LeukemiaMatcher(DisorderMatcher):
    """
    The `eds.leukemia` pipeline component extracts mentions of leukemia.

    ??? info "Details of the used patterns"
        ```{ .python .no-check }
        # fmt: off
        --8<-- "edsnlp/pipelines/ner/disorders/leukemia/patterns.py"
        # fmt: on
        ```

    Extensions
    ----------
    On each span `span` that match, the following attributes are available:

    - `span._.detailed_status`: set to `"PRESENT"`

    Examples
    --------
    ```python
    import edsnlp

    nlp = edsnlp.blank("eds")
    nlp.add_pipe("eds.sentences")
    nlp.add_pipe(
        "eds.normalizer",
        config=dict(
            accents=True,
            lowercase=True,
            quotes=True,
            spaces=True,
            pollution=dict(
                information=True,
                bars=True,
                biology=True,
                doctors=True,
                web=True,
                coding=True,
                footer=True,
            ),
        ),
    )
    nlp.add_pipe(f"eds.leukemia")
    ```

    Below are a few examples:

    --8<-- "docs/assets/fragments/leukemia-examples.md"

    Parameters
    ----------
    nlp : Optional[PipelineProtocol]
        The pipeline
    name : Optional[str]
        The name of the component
    patterns: Union[Dict[str, Any], List[Dict[str, Any]]]
        The patterns to use for matching
    label : str
        The label to use for the `Span` object and the extension
    span_setter : SpanSetterArg
        How to set matches on the doc

    Authors and citation
    --------------------
    The `eds.leukemia` component was developed by AP-HP's Data Science team with a team
     of medical experts. A paper describing in details the development of those
     components is being drafted and will soon be available.
    """

    def __init__(
        self,
        nlp: Optional[PipelineProtocol] = None,
        name: str = "eds.leukemia",
        *,
        patterns: Union[Dict[str, Any], List[Dict[str, Any]]] = default_patterns,
        label: str = "leukemia",
        span_setter: SpanSetterArg = {"ents": True, "leukemia": True},
    ):
        super().__init__(
            nlp=nlp,
            name=name,
            patterns=patterns,
            label=label,
            span_setter=span_setter,
        )

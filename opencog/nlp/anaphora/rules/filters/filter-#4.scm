;; anaphor is "masculine"
;; antecedent is "feminine"

(define filter-#4
    (BindLink
        (ListLink
            (TypedVariableLink
                (VariableNode "$word-inst-antecedent")
                (VariableTypeNode "WordInstanceNode")
            )
            (TypedVariableLink
                (VariableNode "$word-inst-anaphor")
                (VariableTypeNode "WordInstanceNode")
            )
        )
        (ImplicationLink
            (AndLink
                ;; Connection between two clauses
                (ListLink
                    (AnchorNode "CurrentResolution")
                    (VariableNode "$word-inst-anaphor")
                    (VariableNode "$word-inst-antecedent")
                )
                (ListLink
                    (AnchorNode "CurrentPronoun")
                    (VariableNode "$word-inst-anaphor")
                )
                (ListLink
                    (AnchorNode "CurrentProposal")
                    (VariableNode "$word-inst-antecedent")
                )

                ;; filter
                (InheritanceLink
                    (VariableNode "$word-inst-anaphor")
                    (DefinedLinguisticConceptNode "masculine")
                )
                (InheritanceLink
                    (VariableNode "$word-inst-antecedent")
                    (DefinedLinguisticConceptNode "feminine")
                )
            )
            (ListLink
                (AnchorNode "CurrentResult")
                (AnchorNode "Filtered")
            )
        )
    )
)

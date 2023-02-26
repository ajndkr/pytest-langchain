def test_chain(llm_chain, test_case):
    """Loads and tests LLMChain"""
    print(test_case)
    chain_input, chain_output = test_case
    assert llm_chain.run(chain_input) == chain_output

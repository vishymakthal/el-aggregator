import React from 'react';

import AutoComplete from './autocomplete/autocomplete.component';
import CompareSearch from './comparesearch/comparesearch.component';

import algoliasearch from 'algoliasearch';
import { connectAutoComplete, connectHitsPerPage, InstantSearch } from 'react-instantsearch-dom';

const searchClient = algoliasearch(
    process.env.REACT_APP_SEARCH_ID,
    process.env.REACT_APP_SEARCH_KEY  
);

const ConnectedAutoComplete = connectAutoComplete(AutoComplete);
const ConnectedCompareSearch = connectHitsPerPage(CompareSearch);

function SearchBox({index, kind}) {
    if (kind === "full") {
        return <AutoComplete />
    }

    if (kind === "compare") {
        return (
            <div className="searchBox">        
                <InstantSearch indexName={index} searchClient={searchClient}>
                    <ConnectedCompareSearch defaultRefinement={''} items={[]}/> 
                </InstantSearch>
            </div>
        )
    }

    return (
        <div className="searchBox">        
            <InstantSearch indexName={index} searchClient={searchClient}>
                <ConnectedAutoComplete indexName={index}/>
            </InstantSearch>
        </div>
    )
};

export default SearchBox;
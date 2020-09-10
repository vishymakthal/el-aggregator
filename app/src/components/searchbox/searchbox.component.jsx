import React from 'react';

import AutoComplete from './autocomplete/autocomplete.component';

import algoliasearch from 'algoliasearch';
import { connectAutoComplete, InstantSearch } from 'react-instantsearch-dom';

const searchClient = algoliasearch(
    process.env.REACT_APP_SEARCH_ID,
    process.env.REACT_APP_SEARCH_KEY  
);

const CustomAutoComplete = connectAutoComplete(AutoComplete);

function SearchBox({index, full}) {
    if (full) {
        return <AutoComplete />
    }

    return (
        <div className="searchBox">        
            <InstantSearch indexName={index} searchClient={searchClient}>
                <CustomAutoComplete indexName={index}/>
            </InstantSearch>
        </div>
    )
};

export default SearchBox;
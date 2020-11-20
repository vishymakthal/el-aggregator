import React from 'react';

import './comparesearch.styles.scss';

function CompareSearch({ items, currentRefinement, refine}) {
  
    return (
      <div className='compareSearch'>  
        <input
              type="search"
              value={currentRefinement}
              placeholder="Search for a player"
              onChange={event => refine(event.currentTarget.value)}
            />
        <div className='compareSearchResults'>      
          {items.map(hit => (
            <div className='compareSearchResult'>
              <a key={hit.sofifa_id} href={`/player/${hit.sofifa_id}`}>{hit.short_name}</a>
            </div>
          ))}
        </div>
      </div>
    )
  
};

export default CompareSearch;
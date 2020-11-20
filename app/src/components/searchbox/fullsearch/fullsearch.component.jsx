import React from 'react';

import './fullsearch.styles.scss';

class FullSearch extends React.Component {
 
   constructor(props) {
       super(props);

       this.state = {
           hits : []
       }
   }

   handleSubmit (event) {
    fetch(`${process.env.REACT_APP_API_URL}/api/v1/`)
   }

   render () {
      <div className='fullSearch'>  
        <input
              type="search"
              placeholder="Search for a player"
            />
        <input 
            className="searchButton"
            type="button"
            onClick={this.handleSubmit}
             />
        <div className='searchResults'>      
          {this.state.hits.map(hit => (
            <div className='searchResult'>
              <img src={`${process.env.REACT_APP_API_URL}/api/v1/images/${hit.sofifa_id}?q=player`}/>
              <a key={hit.sofifa_id} href={`/player/${hit.sofifa_id}`}>{hit.short_name}</a>
            </div>
          ))}
        </div>
      </div>
    };
};

export default FullSearch;
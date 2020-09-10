import React from 'react';

import './teampage.styles.scss';

class TeamPage extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            name : "",
            players : [],
            id: 0, 
        }
    }

    async componentDidMount() {
        fetch(`https://el-aggregator-api-q3hl2qd3ia-uk.a.run.app/api/v1/players/?team=${this.props.match.params.name}`, {method: 'GET'})
            .then(response => response.json())
            .then(players => this.setState({players : players}));
    }

    render () {
        
        const name = this.props.match.params.name.toUpperCase();
        const img = `https://el-aggregator-api-q3hl2qd3ia-uk.a.run.app/api/v1/images/${this.props.match.params.id}?q=team`;
        const players = Object.keys(this.state.players).map((key, ix) =>
                    <div className='searchResult'>
                        <img alt={key} src={`https://el-aggregator-api-q3hl2qd3ia-uk.a.run.app/api/v1/images/${key}?q=player`}/>
                        <a key={key} href={`/player/${key}`}>{this.state.players[key].short_name}</a>
                    </div>
                    );
        return(
            <div className='teamPage'>
                <h1>{name}</h1>
                <img src={img} alt={name} className='teamImg'/>
                <ul>
                    {players}
                </ul> 
            </div>
       )
    }
}

export default TeamPage;
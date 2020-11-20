import React from 'react';

import ProfileSection from '../../components/player/profile-section/profile-section.component';
import FifaSection from '../../components/player/fifa-section/fifa-section.component';
import HighlightSection from '../../components/player/highlight-section/highlight-section.component';


import './playerpage.styles.scss';

class PlayerPage extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            playerData : null,
            youtubePreview: null,
        }
    }

    getData() {
        fetch(`${process.env.REACT_APP_API_URL}/api/v1/players/${this.props.match.params.id}`, {method: 'GET'})
        .then(response => response.json())
        .then(player => this.setState({playerData : player}));
       
    }

    render () {

        this.getData();
        const playerData = this.state.playerData;
        if (playerData) {
            playerData.id = this.props.match.params.id; 
            playerData.img = `${process.env.REACT_APP_API_URL}/api/v1/images/${this.props.match.params.id}?q=player`;
        }
        const youtubePreview = this.state.youtubePreview;

        return(

            <div className='playerPage'>
                <div className='dataSection'>
                    <ProfileSection playerData={playerData} />
                </div>
                <FifaSection playerData={playerData} />
                {/* {playerData ? <HighlightSection playerData={playerData} youtubePreview={youtubePreview}/> : <br/> } */}
            </div>
        )
    }
}

export default PlayerPage;
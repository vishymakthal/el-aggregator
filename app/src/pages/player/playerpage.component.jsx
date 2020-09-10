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

    componentWillMount() {
        fetch(`https://el-aggregator-api-q3hl2qd3ia-uk.a.run.app/api/v1/players/${this.props.match.params.id}`, {method: 'GET'})
        .then(response => response.json())
        .then(player => this.setState({playerData : player, youtubePreview: player.youtube.highlights[0]}));
       
    }

    render () {

        const playerData = this.state.playerData;
        if (playerData) {
            playerData.id = this.props.match.params.id; 
            playerData.img = `https://el-aggregator-api-q3hl2qd3ia-uk.a.run.app/api/v1/images/${this.props.match.params.id}?q=player`;
        }
        const youtubePreview = this.state.youtubePreview;

        return(

            <div className='playerPage'>
                <div className='dataSection'>
                    <ProfileSection playerData={playerData} />
                    <FifaSection playerData={playerData} />
                </div>
                {playerData ? <HighlightSection playerData={playerData} youtubePreview={youtubePreview}/> : <br/> }
            </div>
        )
    }
}

export default PlayerPage;
import React from 'react';
import Skeleton, { SkeletonTheme } from 'react-loading-skeleton';

import './profile-section.styles.scss';
import tm from './tm.jpeg';
import sf from './sf.png';
import w  from './wiki.png'

const LinkBar = ({tm_url, sf_url, w_url}) => (
    <div className='linkBar'>
        <a href={tm_url}>
            <img src={tm} className='iconImg' alt='transfermarkt' target='_blank' />
        </a>
        <a href={sf_url}>
            <img src={sf} className='iconImg' alt='sofifa' target='_blank' />
        </a>
        <a href={w_url}>
            <img src={w} className='iconImg' alt='wikipedia' target='_blank' /> 
        </a>
    </div>
);
const ProfileSection = ({playerData}) => (
    <>

        {playerData ? 
            <div className='profileSection'>
                <h3>{playerData.long_name}</h3>
                <img className='playerImg' alt={playerData.short_name} src={playerData.img} />
                <br/>
                <b>{playerData.club} | {playerData.nationality}</b>
                <p>{playerData.age} | {playerData.player_positions}</p>
                <p>{playerData.wiki.bio}</p>
                <LinkBar tm_url={playerData.transfermarkt.url} sf_url={playerData.player_url} w_url={playerData.wiki.url}/>
                <br/>
            </div>
                :
            <div className='profileSection'>
                <SkeletonTheme>                
                    <h3><Skeleton /></h3>
                    <br/>
                    <Skeleton circle={true} height={120} width={120} />
                    <Skeleton />
                    <br/>
                    <p><Skeleton count={3} /></p>
                </SkeletonTheme>
            </div>
                }
            
            </>
);

export default ProfileSection;
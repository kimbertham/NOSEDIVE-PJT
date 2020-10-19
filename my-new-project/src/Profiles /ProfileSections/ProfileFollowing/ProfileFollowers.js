import React from 'react'
import { defaultImage } from '../../../lib/commonFiles'


const ProfileFollowers = ( { getData, user }) => {
  const { followers } = user

  if (!followers ) return ''
  return (

    <div className='followers-container fill-width flex'>
      
      {followers.map(follower => {
        return (

          <div
            onClick={() => getData(follower.user_from.id)}
            key={follower.id} 
            className='follow-field dark-border'>

            <div 
              className="follow-pic" 
              style ={ { backgroundImage: `url(${follower.user_from.profile_image ? 
                follower.user_from.profile_image : defaultImage})` } }/>

            <h1 
              className='italic'> 
              {follower.user_from.first_name} {follower.user_from.last_name}
            </h1>

            <small> 
                Friends since {follower.created.split('-').reverse().join(' ')}
            </small>

          </div>
        )
      })}

    </div>

  )
}

export default ProfileFollowers
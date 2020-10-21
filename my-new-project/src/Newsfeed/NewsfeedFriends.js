import React from 'react'
import { Link } from 'react-router-dom'

const NewsfeedFriends = ({ friends }) =>  {


  return (
    <div className='bordered-box'>
      <h2 className='feed-title dark-border'> Friends of friends</h2>
      <div className= 'find-cont center'>
        {friends.map(friend => {
          return <div 
            key={friend.id}
            className='friend-cont center italic '>
            <Link to={`/profile/${friend.id}/activity`}>
              <div style={{
                backgroundImage: `url(${friend.profile_image})`
              }} className=' friend-icon profile-image '/>

              <p> {friend.first_name} {friend.last_name}</p>
              <p>@{friend.username}</p>
            </Link>
            <button className='button follow-button'>Follow</button>
          </div>
        
  
        })}
      </div>
    </div>

  )
}

export default NewsfeedFriends
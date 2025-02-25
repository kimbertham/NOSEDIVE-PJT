import React from 'react'

const Logo = () => {
  return (
    <div className='logo-set column center'>
      <div>
        <img src={require('../styles/assets/logo-n.jpg')}/>
        <img src={require('../styles/assets/o.jpg')}
          className='logo-o'alt='logo'/>
        <img  src={require('../styles/assets/logo-sins.jpg')}
          alt='logo'/>
      </div>
    </div>
  )
}

export default Logo
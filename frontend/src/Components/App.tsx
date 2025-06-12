import { useState } from 'react'
import '../styles/App.css'
import Input from './Input'
import Map from './MapComponent/Map'
import Word from './Word'

function App() {

  return (
    <>

      <div className="main-body">
        <nav>Navigation</nav>
        <h1>Welcome to <em>Raizr</em></h1>
        <Input />
        <Map />
      </div>

    </>
  )
}

export default App

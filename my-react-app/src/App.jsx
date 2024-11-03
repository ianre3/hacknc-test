import { useState } from 'react'
{/*import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'*/}
import './App.css'
import './gpt.js'

function App() {
  const [count, setCount] = useState(0)
  const [object1, setObject1] = useState('');
  const [object2, setObject2] = useState('');
  {/*const [age, setAge] = useState('20');
  const ageAsNumber = Number(age);*/}
  function afterInput(value) {
    console.log(value)
  }

  return (
    <>
      <div>
        {/*<a target="_blank">
          <img src={"https://mobileimages.lowes.com/marketingimages/2b928fb1-a997-4a2c-8824-4b149b75b8ef/lowes-logos-dp18-332098-og.jpg"}
          className="logo"
          alt="vitelogo"
          {/*style={styles.cover} />
        </a>*/}
        <a href="https://www.lowes.com/" target="_blank">
          <img src={"https://www.lowescdn.com/images/logos/Lowes_logo_CMYK_blue.png"} className="logo" alt="Vite logo" />
        </a>
      </div>
      {/*<div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>*/}
      <h1>Nail it with Lowe's!</h1>
       {/*<div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Tell us more information!
      </p>*/}

      <div>
        <label> 
          What would you like to build today?   
          <input className="input"
            value={object1}
            onChange={e => setObject1(e.target.value)}
            onKeyUp={event => {
              if (event.key === 'Enter') {
                afterInput({object1})}}
              }
          />
        </label>
      </div>
      
      {/*<label>
        Age:
        <input
          value={age}
          onChange={e => setAge(e.target.value)}
          type="number"
        />
        <button onClick={() => setAge(ageAsNumber + 10)}>
          Add 10 years
        </button>
      </label>*/}

      {/*{ageAsNumber > 0 &&
        <p>Your recommended materials are {ageAsNumber}.</p>
      }*/}

      <div>
        <label> 
          What are the dimensions of your project?  (in x in) 
          <input className="input"
            value={object2}
            onChange={e => setObject2(e.target.value)}
            onKeyUp={event => {
              if (event.key === 'Enter') {
                afterInput({object2})}}
              }
          />
        </label>
      </div>
      {/*
      {object1 !== '' &&
        <p>Your recommended materials are {object1}.</p>
      }
      {object2 !== '' &&
        <p>Your recommended material quantity is {object2}.</p>
      }
      */}
      <div>
        <p>getProjectMaterials({object1})</p>
      </div>
      
    </>
  )

}

export default App

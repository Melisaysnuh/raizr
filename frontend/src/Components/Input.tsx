import React, { useState } from "react"
import '../styles/Input.css'

const Input: React.FC = () => {
  const [word, setWord] = useState("")

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>)=> {
    event.preventDefault()
    const form = event.currentTarget
    const input = form.elements.namedItem("word-input") as HTMLInputElement
    console.log(input.value)
    // call backend with value
  }

  return (
    <>
    <form id="input-form" onSubmit={handleSubmit}>
        <label className="word-input" htmlFor="word-input">Enter a word to start finding roots.</label>
        <input id="word-input" name="word-input" type="text"></input>

      <button >Search</button>
    </form>

    </>
  )
}

export default Input

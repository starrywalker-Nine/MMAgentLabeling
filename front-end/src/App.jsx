// react imports
import { useState } from 'react'

// library imports
import JSConfetti from 'js-confetti'
import { BrowserRouter, Link, Route } from "react-router-dom";
// const jsConfetti = new JSConfetti()
// jsConfetti.addConfetti()

// custom component imports
// 自定义组件命名必须大写
// import CustomForm from './components/CustomForm'
// import OneThing from './components/OneThing'
import Index from './pages/home/_index.jsx'

// function getSuccessMessage(){
//   const message = ['恭喜你完成了任务！', '你真棒！', '你做的很棒！', '你做的很好！', 'good job!', 'well done!',
//     'amazing!', 'excellent!', 'great!', 'fantastic!', 'wonderful!', 'outstanding!', 'fantabulous!',
//     'incredible!', 'wonderful!', 'wow!'
//   ]
//   return message[Math.floor(Math.random() * message.length)]
// }

function App() {
  // const [count, setCount] = useState(0)
  // const [thing, setThing] = useState('')
  // const [isCompleted, setIsCompleted] = useState(true)

  // const handleSumbmit = (e) => {
  //   e.preventDefault()
  //   // 点击是消失
  //   setIsCompleted(false)
  //   // console.log('submit')
  // }
  // const handleInput = (e) => {
  //   // console.log(e.target.value)
  //   setThing(e.target.value)
  // }

  // const handleCompleteThing = async (e) => {
  //   // e.preventDefault()
  //   e.target.setAttribute('disabled', true);
  //   setThing(getSuccessMessage());
  //   const jsConfetti = new JSConfetti()
  //   jsConfetti.addConfetti()
  //   await jsConfetti.addConfetti({
  //     emojis: ['🌈', '⚡️', '💥', '✨', '💫', '🌸'],
  //  })
  //  e.target.removeAttribute('disabled');
  //  setThing('')
  //  setIsCompleted(true)
  // }

  return (
    <>
      <div>
        <BrowserRouter>
        <Link to="/index">首页</Link>
          <Routes basename="/">
            <Route path="/index" element={<Index />}>
            {/* index 默认路由 */}
              <Route index element={<Index />}/>
            </Route>
          </Routes>
        </BrowserRouter>
      </div>
      {/* <main className="grid place-items-center min-h-screen bg-gradient-to-b from-slate-100 to-slate-200
      dark:from-slate-800 dark:to-slate-900 text-slate-900 dark:text-slate-100
      ">
        <div className='grid place-items-center gap-8 m-8'>
        { isCompleted && (<CustomForm 
        thing={thing} 
        handleSumbmit={handleSumbmit} 
        handleInput={handleInput}
        />
        )}
        {
          !isCompleted && (
            <OneThing thing={thing} 
            handleCompleteThing={handleCompleteThing}
            />
          )
        }
        </div>
      </main> */}

    </>
  )
}

export default App

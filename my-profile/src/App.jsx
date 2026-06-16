import { useState } from 'react'
import Header from './Header'
import SkillTag from './SkillTag'
import Footer from './Footer'
import './App.css'

function App() {
  const [skills, setSkills] = useState([
    'Python — Assert, Pytest, Parametrize',
    'Playwright — Form Testing, Screenshot อัตโนมัติ',
    'API Testing — GET, POST, PUT, DELETE',
    'CI/CD — Git, GitHub, GitHub Actions',
  ])

  function addSkill() {
    setSkills([...skills, 'React — Coming Soon'])
  }

  function removeSkill() {
    setSkills(skills.slice(0, -1))
  }

  return (
    <div>
      <Header />
      <main style={{ maxWidth: '800px', margin: '40px auto', padding: '0 20px' }}>
        <section>
          <h2>ทักษะ</h2>
          <ul style={{ display: 'flex', flexWrap: 'wrap', gap: '8px', padding: 0 }}>
            {skills.map((skill) => (
              <SkillTag key={skill} name={skill} />
            ))}
          </ul>
          <button onClick={addSkill}>เพิ่ม React</button>
          <button onClick={removeSkill}>ลบ Skill</button>
        </section>
      </main>
      <Footer />
    </div>
  )
}

export default App
function Header() {
  return (
    <header style={{
      background: '#7700ff',
      color: 'white',
      padding: '20px 40px',
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
    }}>
      <h1 style={{ margin: 0, fontSize: '28px' }}>เรา เต๋าเองนะ</h1>
      <p style={{ margin: 0, fontSize: '14px', opacity: 0.8 }}>
        QA Automation Engineer
      </p>
    </header>
  )
}

export default Header
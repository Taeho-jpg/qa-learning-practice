function SkillTag({ name }) {
  return (
    <li style={{
      background: '#7700ff',
      color: 'white',
      padding: '6px 14px',
      borderRadius: '20px',
      listStyle: 'none',
      fontSize: '13px',
    }}>
      {name}
    </li>
  )
}

export default SkillTag
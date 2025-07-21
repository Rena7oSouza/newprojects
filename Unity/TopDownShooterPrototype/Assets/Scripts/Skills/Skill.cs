using UnityEngine;

[CreateAssetMenu(fileName = "NewSkill", menuName = "Skills/Skill")]
public class Skill : ScriptableObject
{
    public string skillName;
    public string description;
    public SkillBonusType bonusType;
    public float bonusValue;
    public int levelRequired;
}

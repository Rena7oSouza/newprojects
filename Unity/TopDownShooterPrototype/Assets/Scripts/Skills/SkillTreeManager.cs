using UnityEngine;

public class SkillTreeManager : MonoBehaviour
{
    public Skill[] unlockedSkills;

    private PlayerStats playerStats;
    private PlayerShooting playerShooting;

    void Awake()
    {
        playerStats = GetComponent<PlayerStats>();
        playerShooting = GetComponent<PlayerShooting>();

        ApplyAllUnlockedSkills();
    }

    /// <summary>
    /// Applies all unlocked skill bonuses at startup.
    /// </summary>
    void ApplyAllUnlockedSkills()
    {
        foreach (Skill skill in unlockedSkills)
        {
            ApplySkillBonus(skill);
        }
    }

    /// <summary>
    /// Applies a specific skill bonus to the correct script.
    /// </summary>
    /// <param name="skill">The skill to apply.</param>
    public void ApplySkillBonus(Skill skill)
    {
        switch (skill.bonusType)
        {
            case SkillBonusType.Health:
                if (playerStats != null)
                {
                    playerStats.maxHealth += (int)skill.bonusValue;
                }
                break;

            case SkillBonusType.Damage:
                if (playerShooting != null)
                {
                    playerShooting.baseDamage += skill.bonusValue;
                }
                break;

            case SkillBonusType.ReloadSpeed:
                if (playerShooting != null)
                {
                    playerShooting.reloadSpeed -= skill.bonusValue;
                }
                break;

            case SkillBonusType.MagazineSize:
                if (playerShooting != null)
                {
                    playerShooting.magazineSize += (int)skill.bonusValue;
                }
                break;

            case SkillBonusType.MoveSpeed:
                if (playerStats != null)
                {
                    playerStats.moveSpeed += skill.bonusValue;
                }
                break;

            // Add new skill bonus types here as needed

            default:
                Debug.LogWarning("Unhandled skill bonus type: " + skill.bonusType);
                break;
        }
    }

    /// <summary>
    /// Returns the unlocked skill with the given name.
    /// </summary>
    /// <param name="skillName">The name of the skill.</param>
    /// <returns>The skill if found, otherwise null.</returns>
    public Skill GetSkill(string skillName)
    {
        foreach (Skill skill in unlockedSkills)
        {
            if (skill.skillName == skillName)
                return skill;
        }
        return null;
    }
}

using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class SkillUpgradeUIManager : MonoBehaviour
{
    public SkillTreeManager skillTreeManager;
    public PlayerStats playerStats;

    public TMP_Text skillPointText;
    public Button pistolButton;
    public TMP_Text pistolLevelText;
    public Button rifleButton;
    public TMP_Text rifleLevelText;
    public Button sniperButton;
    public TMP_Text sniperLevelText;

    public GameObject panel;

    void Start()
    {
        UpdateUI();

        pistolButton.onClick.AddListener(() => UpgradeSkill("Pistol Mastery"));
        rifleButton.onClick.AddListener(() => UpgradeSkill("Rifle Mastery"));
        sniperButton.onClick.AddListener(() => UpgradeSkill("Sniper Mastery"));
    }

    void UpdateUI()
    {
        skillPointText.text = "Skill Points: " + playerStats.skillPoints;

        pistolLevelText.text = "Lv " + skillTreeManager.GetSkill("Pistol Mastery").currentLevel;
        rifleLevelText.text = "Lv " + skillTreeManager.GetSkill("Rifle Mastery").currentLevel;
        sniperLevelText.text = "Lv " + skillTreeManager.GetSkill("Sniper Mastery").currentLevel;
    }

    public void UpgradeSkill(string skillName)
    {
        if (playerStats.skillPoints > 0)
        {
            Skill skill = skillTreeManager.GetSkill(skillName);
            if (skill != null)
            {
                skill.currentLevel++;
                playerStats.skillPoints--;

                skillTreeManager.ApplySkillBonus(skill);
                UpdateUI();
            }
        }
    }

    public void OpenPanel()
    {
        panel.SetActive(true);
        UpdateUI();
    }

    public void ClosePanel()
    {
        panel.SetActive(false);
    }
}

using UnityEngine;

public class PlayerStats : MonoBehaviour
{
    public static PlayerStats Instance;

    public int level = 1;
    public int exp = 0;
    public int expToNextLevel = 100;
    public int damage = 1; // Base damage
    public float maxHealth = 100f;

    public float moveSpeed = 1f;

    public int skillPoints = 0;

    void Awake()
    {
        if (Instance == null)
            Instance = this;
        else
            Destroy(gameObject);
    }

    public void GainExp(int amount)
    {
        exp += amount;
        CheckLevelUp();
    }

    void CheckLevelUp()
    {
        while (exp >= expToNextLevel)
        {
            exp -= expToNextLevel;
            LevelUp();
        }
    }

    void LevelUp()
    {
        level++;
        expToNextLevel = Mathf.RoundToInt(expToNextLevel * 1.5f);
        damage++; // Increase damage per level
        skillPoints++;
        Debug.Log("Level Up! Now level: " + level);
    }
}

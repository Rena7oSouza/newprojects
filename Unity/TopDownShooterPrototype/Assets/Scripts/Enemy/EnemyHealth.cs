using UnityEngine;
using UnityEngine.UI;

public class EnemyHealth : MonoBehaviour
{
    public EnemyInfo data; // Drag your EnemyInfo ScriptableObject here

    private float currentHealth;

    public GameObject healthBarPrefab;
    private GameObject healthBarInstance;
    private Image healthBarFill;
    private PlayerStats playerStats;


    void Start()
    {
        if (data == null)
        {
            Debug.LogError("EnemyInfo data is missing!");
            return;
        }

        currentHealth = data.maxHealth;
        playerStats = GameObject.FindGameObjectWithTag("Player").GetComponent<PlayerStats>();


        // Instantiate health bar as independent object in scene
        healthBarInstance = Instantiate(healthBarPrefab, transform.position + new Vector3(0, 0.5f, 0), Quaternion.identity);
        healthBarFill = healthBarInstance.transform.Find("HealthBarFill").GetComponent<Image>();
    }

    void Update()
    {
        if (healthBarInstance != null)
        {
            // Update health bar position and keep it upright
            healthBarInstance.transform.position = transform.position + new Vector3(0, 0.5f, 0);
            healthBarInstance.transform.rotation = Quaternion.identity;
        }
    }

    public void TakeDamage(float damage)
    {
        currentHealth -= damage;
        UpdateHealthBar();

        if (currentHealth <= 0)
        {
            Die();
        }
    }

    void UpdateHealthBar()
    {
        if (healthBarFill != null)
        {
            float fillAmount = (float)currentHealth / data.maxHealth;
            healthBarFill.fillAmount = fillAmount;

            Color healthColor;

            if (fillAmount > 0.5f)
            {
                // Green to Yellow
                healthColor = Color.Lerp(Color.yellow, Color.green, (fillAmount - 0.5f) * 2f);
            }
            else
            {
                // Yellow to Red
                healthColor = Color.Lerp(Color.red, Color.yellow, fillAmount * 2f);
            }

            healthBarFill.color = healthColor;
        }
    }

    void Die()
    {
        // Death effect
        if (data.deathEffectPrefab != null)
            Instantiate(data.deathEffectPrefab, transform.position, Quaternion.identity);

        // Drop loot
        LootManager.DropLoot(data, transform.position);

        // Destroy health bar and enemy
        if (healthBarInstance != null)
            Destroy(healthBarInstance);
            
        //Send EXP to Player
        if (playerStats != null)
        {
            playerStats.GainExp(data.expReward);
        }

        Destroy(gameObject);
    }
}

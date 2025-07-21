using UnityEngine;

[CreateAssetMenu(fileName = "NewEnemyInfo", menuName = "Enemies/Enemy Info")]
public class EnemyInfo : ScriptableObject
{
    [Header("Basic Stats")]
    public string enemyName;
    public int maxHealth = 10;
    public int damage = 1;
    public int expReward = 20;

    [Header("Movement")]
    public float moveSpeed = 2f;
    public float stoppingDistance = 1.5f;

    [Header("Loot Table")]
    public LootData[] lootTable;

    [Header("Visuals")]
    public GameObject deathEffectPrefab;
}

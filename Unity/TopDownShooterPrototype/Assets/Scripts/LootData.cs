using UnityEngine;

[System.Serializable]
public class LootData
{
    public GameObject itemPrefab; // The item to drop
    public int minQuantity = 1;
    public int maxQuantity = 1;

    [Range(0, 100)]
    public float dropChance = 100f; // Used when maxQuantity <= 1

    [Tooltip("Drop chance decays by this % per extra item above minQuantity.")]
    public float decayRate = 2f; // Percent decrease per additional item if maxQuantity > 1
}

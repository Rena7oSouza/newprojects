using UnityEngine;

[System.Serializable]
public class Wave
{
    public WaveType waveType;
    public int enemyCount; // Used for KillCount
    public float duration; // Used for Timed
    public float spawnInterval; // Time between spawns
}

using UnityEngine;

public class ImpactEffect : MonoBehaviour
{
    public float lifeTime = 0.5f;

    void Start()
    {
        Destroy(gameObject, lifeTime);
    }
}

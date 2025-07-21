using UnityEngine;

public class MuzzleFlash : MonoBehaviour
{
    void Start()
    {
        Destroy(gameObject, 0.1f);
    }
}

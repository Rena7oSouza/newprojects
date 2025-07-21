using UnityEngine;

public class AudioManager : MonoBehaviour
{
    public static AudioManager Instance;

    public AudioSource audioSource;
    public AudioClip shootClip;

    void Awake()
    {
        Instance = this;
    }

    public void Play(string clipName)
    {
        switch (clipName)
        {
            case "Shoot":
                audioSource.PlayOneShot(shootClip);
                break;
        }
    }
}

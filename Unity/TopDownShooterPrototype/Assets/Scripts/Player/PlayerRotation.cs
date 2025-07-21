using UnityEngine;
using UnityEngine.InputSystem;

public class PlayerRotation : MonoBehaviour
{
    public SimpleJoystick joystick; // Reference to your virtual joystick
    SimulateMobile simulateMobile; // Enable this in Inspector to test mobile input in Editor

    PlayerControls controls;
    Vector2 aimDirection;

    void Awake()
    {
        controls = new PlayerControls();

        // For PC mouse aim
        controls.Player.Aim.performed += ctx => aimDirection = ctx.ReadValue<Vector2>();
        controls.Player.Aim.canceled += ctx => aimDirection = Vector2.zero;
        simulateMobile = GetComponent<SimulateMobile>();

    }

    void OnEnable()
    {
        controls.Enable();
    }

    void OnDisable()
    {
        controls.Disable();
    }

    void Update()
    {
#if UNITY_STANDALONE || UNITY_EDITOR
        if (!simulateMobile.simulateMobile)
        {
            RotateToMouse();
        }
#endif

#if UNITY_ANDROID || UNITY_IOS
        RotateWithJoystick();
#endif

        // If simulating mobile in Editor
        if (simulateMobile.simulateMobile)
        {
            RotateWithJoystick();
        }
    }

    void RotateToMouse()
    {
        Vector3 mousePos = Mouse.current.position.ReadValue();
        Vector3 mouseWorldPos = Camera.main.ScreenToWorldPoint(new Vector3(mousePos.x, mousePos.y, Camera.main.nearClipPlane));

        mouseWorldPos.z = transform.position.z; // Ensure same Z

        Vector3 direction = mouseWorldPos - transform.position;
        float angle = Mathf.Atan2(direction.y, direction.x) * Mathf.Rad2Deg; // NO -90f since sprite points right
        transform.rotation = Quaternion.Euler(0, 0, angle);
    }


    void RotateWithJoystick()
    {
        if (joystick != null)
        {
            Vector2 joyDir = new Vector2(joystick.Horizontal(), joystick.Vertical());
            if (joyDir.sqrMagnitude > 0.01f)
            {
                float angle = Mathf.Atan2(joyDir.y, joyDir.x) * Mathf.Rad2Deg; // Removed -90f
                transform.rotation = Quaternion.Euler(0, 0, angle);
            }
        }
    }

}

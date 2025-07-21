using UnityEngine;
using UnityEngine.EventSystems;

public class SimpleJoystick : MonoBehaviour, IDragHandler, IPointerUpHandler, IPointerDownHandler
{
    private RectTransform bgRect;
    private RectTransform handleRect;
    private Vector2 inputVector;
    public float drift = 0.1f;

    void Start()
    {
        bgRect = GetComponent<RectTransform>();
        handleRect = transform.GetChild(0).GetComponent<RectTransform>();
        inputVector = Vector2.zero;
        handleRect.anchoredPosition = Vector2.zero;
    }

    public void OnDrag(PointerEventData eventData)
    {
        Vector2 pos;
        if (RectTransformUtility.ScreenPointToLocalPointInRectangle(bgRect, eventData.position, eventData.pressEventCamera, out pos))
        {
            pos.x = (pos.x / bgRect.sizeDelta.x);
            pos.y = (pos.y / bgRect.sizeDelta.y);

            inputVector = new Vector2(pos.x * 2, pos.y * 2);
            inputVector = (inputVector.magnitude > 1.0f) ? inputVector.normalized : inputVector;

            handleRect.anchoredPosition = new Vector2(
                inputVector.x * (bgRect.sizeDelta.x / 2),
                inputVector.y * (bgRect.sizeDelta.y / 2)
            );
        }
    }

    public void OnPointerDown(PointerEventData eventData)
    {
        OnDrag(eventData);
    }

    public void OnPointerUp(PointerEventData eventData)
    {
        inputVector = Vector2.zero;
        handleRect.anchoredPosition = Vector2.zero;
    }

    // 🔷 Public wrappers for EventTrigger
    public void PointerDown(BaseEventData data)
    {
        OnPointerDown((PointerEventData)data);
    }

    public void PointerUp(BaseEventData data)
    {
        OnPointerUp((PointerEventData)data);
    }

    public void Drag(BaseEventData data)
    {
        OnDrag((PointerEventData)data);
    }

    public float Horizontal()
    {
        return inputVector.x;
    }

    public float Vertical()
    {
        return inputVector.y;
    }

    public Vector2 Direction()
    {
        return inputVector;
    }
}

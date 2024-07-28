using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using DG.Tweening;

public class GameManager : MonoBehaviour
{
    [SerializeField] private PlayerController _playerController;
    [SerializeField] private Camera _worldCamera;
    [SerializeField] private AudioClip _worldMusic;
    [SerializeField] private Image _transitionPanel;

    private GameState _gameState;

    public static GameManager SharedInstance;

    private void Start() {

        DialogManager.SharedInstance.OnDialogStart += () => _gameState = GameState.Dialog;
        DialogManager.SharedInstance.OnDialogFinish += () => _gameState = GameState.Travel;

        _transitionPanel.color = new Color32(0x00, 0x00, 0x00, 0xff);

        StartCoroutine(FadeToWorld());
    }

    private void Update() {
        switch(_gameState)
        {
            case GameState.Dialog:
                DialogManager.SharedInstance.HandleUpdate();
                break;

            case GameState.Travel:
                _playerController.HandleUpdate();
                break;
        }
    }

    private IEnumerator FadeToWorld()
    {
        _gameState = GameState.Travel;

        yield return _transitionPanel.DOFade(1, 0.4f).WaitForCompletion();

        _worldCamera.gameObject.SetActive(true);

        AudioManager.SharedInstance.PlayMusic(_worldMusic);

        yield return _transitionPanel.DOFade(0, 0.4f).WaitForCompletion();
    }
}

public enum GameState
{
    Battle,
    CutScene,
    Dialog,
    Travel,
}

import time
import unittest
import cv2
from capture import VideoCapture

class VideoCaptureTest(unittest.TestCase):
    def setUp(self):
        print("[i] Configurando o teste.")

    def _run(self, width=1280, height=720, with_threading=False):
        print(f"[i] Iniciando o teste com threading={with_threading}")
        
        if with_threading:
            cap = VideoCapture("pessoas1.mp4")
        else:
            cap = cv2.VideoCapture("pessoas1.mp4")
        
        # Obtém o número total de quadros do vídeo
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f"[i] Número total de quadros: {total_frames}")
        
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        
        if with_threading:
            cap.start()
        
        t0 = time.time()
        
        i = 0
        while i < total_frames:
            grabbed, frame = cap.read()
            if not grabbed:
                print("[i] Nenhum quadro capturado. Saindo do loop.")
                break
            
            if frame is not None:
                cv2.imshow('Frame', frame)
                cv2.waitKey(1) & 0xFF
            else:
                print("[i] Quadro vazio detectado.")
            
            i += 1
        
        print('[i] Frames por segundo: {:.2f}, com threading={}'.format(total_frames / (time.time() - t0), with_threading))
        
        if with_threading:
            cap.stop()
        
        cv2.destroyAllWindows()

    def test_video_capture(self):
        print("[i] Executando teste sem threading.")
        self._run(1280, 720, False)

    def test_video_capture_threading(self):
        print("[i] Executando teste com threading.")
        self._run(1280, 720, True)

if __name__ == '__main__':
    unittest.main()

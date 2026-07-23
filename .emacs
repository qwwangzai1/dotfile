(global-display-line-numbers-mode 1)
(setq-default cursor-type 'bar)
(recentf-mode 1)
(tool-bar-mode 0)
(defvar term-name "*terminal*")

(defun get-term ()
  (if (get-buffer term-name)
      (switch-to-buffer term-name)
    (ansi-term "bash" "terminal")))


(defun my-compile-and-run ()
  (interactive)
  (save-buffer)
  (let* ((file (buffer-file-name))
         (base (file-name-sans-extension file)))
    (get-term)
    (term-send-raw-string "clear\n")
    (term-send-raw-string (format "g++ -std=c++17 -Wall -o %s '%s' && %s\n" base file base))))

(defun python-run ()
  (interactive)
  (save-buffer)
  (let ((file (buffer-file-name)))
    (get-term)
    (term-send-raw-string "clear\n")
    (term-send-raw-string (format "python3 %s\n" file))))

(add-hook 'c++-mode-hook (lambda ()
			   (local-set-key (kbd "<f5>") 'my-compile-and-run)))

(add-hook 'python-mode-hook (lambda ()
			      (local-set-key (kbd "<f5>") 'python-run)))

(add-hook 'window-setup-hook
	  (lambda ()
	    (when recentf-list
	      (recentf-open-files))))

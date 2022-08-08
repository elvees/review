====================
Сообщения к коммитам
====================

.. highlight:: none

О документе
===========

Документ описывает правила оформления сообщений к коммитам (commit message)
в репозитории с исходными кодами.

Структура сообщения
===================

#. Сообщение к коммиту может состоять из трёх блоков:

   #. `Блок краткого описания коммита`_.
   #. `Блок подробного описания коммита`_.
   #. `Блок метаинформации`_.

#. Блоки должны быть отделены друг от друга одной пустой строкой.
#. Строки сообщения не должны заканчиваться пробелами и/или табами (trailing whitespaces).

Обобщённый пример сообщения к коммиту::

  prefix: First line with short description

  Подробное описание коммита.

  Второй параграф подробного описания коммита.

  Блок метаинформации (включая следующий Change-Id)
  Change-Id: Ia25e1cbb8c304bf5730cb2f748bcb52e1fa5543b

Блок краткого описания коммита
==============================

#. Блок является обязательным.
#. Блок состоит из одной первой строки сообщения к коммиту длиной не более 65 символов.
#. Блок должен быть написан на английском языке.
#. Блок должен быть написан в настоящем времени в повелительном наклонении
   (т.о. занимает меньше символов).
#. Желательно, чтобы блок состоял из одного предложения.
#. Блок должен быть написан с заглавной буквы.
#. Если блок состоит из одного предложения, точка в конце не ставится.
#. Если блок состоит из нескольких предложений, точки ставятся в конце каждого предложения
   (включая последнее).
#. Блок описывает суть изменения в репозитории.

   Не рекомендуется обобщать изменение, описывать влияние на проект
   и последствия,
   если не описана суть изменения.

   Неправильно::

     Fix error in foo test

   Правильно::

     Increase timeout in foo test

#. Первым словом блока может быть префикс в формате "prefix: ".
#. Префикс может не ставиться, если проект маленький и его нецелесообразно разбивать на
   логические части.
#. Префиксы должны обозначать логические подсистемы, к которым относится коммит, например: usb,
   uvc, hid, dma и т.д. Можно выделить специальные префиксы: build --- для всего, что касается
   сборки проекта; ci --- для всего, что касается непрерывной интеграции.
   Желательно не мельчить и выделять достаточно крупные логические для префиксов ---
   если делать свой префикс для каждого файла, смысл префиксов теряется.

Блок подробного описания коммита
================================

#. Блок является обязательным, за исключением коммитов:

   * выпуск релиза;
   * исправление опечаток;
   * добавление описания новой сущности в документацию.

#. Блок может быть написан на русском языке.
#. Блок не должен повторять краткое описание.
#. Блок может состоять из нескольких параграфов.
#. Параграфы блока должны разделяться пустой строкой.
#. Длина строки должна быть не более 72 символов (за исключением URL-ссылок и логов сообщений).
#. Блок должен содержать причину внесения изменений в проект:
   должно быть понятно, *почему* коммит следует принять в репозиторий.
#. Рекомендуемая структура блока:

   #. Описание проблемы.
   #. Описание подхода к решению проблемы.
   #. Описание того, как данный коммит решает проблему.

   Например::

     foobar: Adjust the foo setting in bar

     When using foobar on systems with less than a gigabyte of RAM common
     usage patterns often result in an Out-of-memory condition causing
     slowdowns and unexpected application termination.

     Low-memory systems should continue to function without running into
     memory-starvation conditions with minimal cost to systems with more
     available memory.  High-memory systems will be less able to use the
     full extent of the system, a dynamically tunable option may be best,
     long-term.

     The foo setting in bar was decreased from X to X-50% in order to
     ensure we don't exhaust all system memory with foobar threads.

     Change-Id: Ie0b8263a2845c17fd68dcc246283b5ed92eff551

#. Списки должны оформляться отдельным параграфом без отступа::

     This is example of list formatting in a commit message:

     * List elements shall have no indentation.
     * List elements shall not extend 70 characters boundary. Longer lines
       shall be wrapped. Line continuation shall be aligned with first
       letter of the first line.
     * If your elements are full paragraphs you may add blank lines between
       them.
     * Nested lists:
       - Are indented with 2 spaces.
       - May use '-' or '+' instead of asterisk.
     * That's all folks!

#. При исправлении ошибок рекомендуется добавлять сообщения об ошибках и логи в сообщение к
   коммиту.

#. Сообщения об ошибках и логи оформляются отдельным параграфом с отступом в два пробела.
   Строки сообщений и логов могут превышать допустимую длину строки и не разбиваются.
   Незначимые строки и части строк сообщения (например, локальные пути среды разработчика)
   рекомендуется заменять троеточием или удалять. Пример::

     The option is deprecated. The priviledge separation is made mandatory.
     The commit removes this option to avoid this warning:

       Starting sshd: /etc/ssh/sshd_config line 110: Deprecated option UsePrivilegeSeparation

   Другой пример::

     dtc produces the next warning when compiling DTS file that contains
     'skip-gpios' property:

       /gpio@38034000/gpio-controller@3: Missing property '#gpio-cells' in node .../uart0_pclk or bad phandle (referred from skip-gpios[0])

#. Гиперссылки должны быть сокращены до якоря "[N]", где N --- число. Якори расшифровываются в
   конце блока отдельным параграфом без отступа. Пример::

     In case of error in start_streaming() all buffers queued in driver
     (in VB2_BUF_STATE_ACTIVE state) must be returned to the V4L2
     subsystem according to [1].

     [1] https://linuxtv.org/downloads/v4l-dvb-apis/kapi/v4l2-videobuf2.html#c.vb2_ops

#. При указании имени функции необходимо использовать скобки после её имени; обобщающее слово
   "function" можно не употреблять::

     A GPIO is requested in dw_spi_child_pre_probe(), but never freed.

#. Если коммит содержит обновление Git-субмодулей, то блок должен содержать список
   новых коммитов в субмодулях в виде списка::

     Update following submodules:

     * submodule1 e171ef7...4d098b9 (2):
       > Commit #1
       > Commit #2

     * submodule2 6bc5811...e2b620c (1):
       > Another commit

   Такой список Git формирует автоматически при редактировании сообщения к коммиту
   в блоке комментариев под сообщением.

Блок метаинформации
===================

#. Блок является необязательным.
#. Блок состоит из одного параграфа.
#. Формат каждой строки параграфа: ``<prefix>: <metadata>``.
#. Допускается многократные вхождения строк с одинаковыми префиксами ``<prefix>:``.
#. Если коммит имеет отношение к задаче таск-трекера, то блок должен содержать ссылку на
   задачу в формате::

     Issue: <reference>
     <reference> ::= <tracker-prefix>#<number> | #<jira-issue-key>
     <tracker-prefix> ::= rf

   Например::

     Issue: rf#867
     Issue: #ASSET-123

   Ссылки соответствуют следующим URL:

   * ``rf#<number>`` --- https://farmer.elvees.com/redmine/issues/<number>
   * ``#<jira-issue-key>`` --- https://jira.elvees.com/browse/<jira-issue-key>

Повторное применение коммитов (cherry-pick)
===========================================

#. При повторном применении коммита последняя строка блока метаинформации должна содержать
   уведомление о повторном применении со ссылкой на оригинальный коммит в формате::

     (cherry picked from commit <commit-SHA>)

#. Для добавления уведомления о повторном применении необходимо использовать команду
   :command:`git cherry-pick -x`. Если команда располагает уведомление о повторном применении
   неправильно, необходимо откорректировать сообщение к коммиту вручную.

#. При повторном применении коммита Change-Id `не должен изменяться
   <https://gerrit-review.googlesource.com/Documentation/intro-user.html#change-id>`_.

#. Если при повторном применении коммита требуется значительное изменение кода, рекомендуется
   оформлять коммит как независимый: не использовать опцию ``-x`` и генерировать новый
   Change-Id.

#. Если блок подробного описание коммита отсутствует, рекомендуется дописать его. Не рекомендуется
   указывать локальные причины применения коммита.

Ссылки
======

* http://habrahabr.ru/post/178355/
* https://www.kernel.org/doc/Documentation/SubmittingPatches
* https://wiki.openstack.org/wiki/GitCommitMessages
* https://www.openembedded.org/wiki/Commit_Patch_Message_Guidelines
* https://www.linux.com/publications/how-participate-linux-community

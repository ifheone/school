# GUI 프로그래밍 1

- 윈도우프로그램 작성시 타이틀바를 포함한 프레임 위에 content pane을 올리고 그 위에 라벨을 붙이는 방식을 이용한다.
- 프레임을 만들 때, JFrame클래스의 객체를 생성한다.
- getContentPane메소드는 content pane을 리턴한다.
- 라벨을 만들 때, JLabel클래스의 객체를 생성한다.
- ContentPane위에 add메소드를 이용해 라벨을 올린다.
- pack메소드는 프레임을 적절한 크기로 만들어 주는 기능을 갖는다.

# GUI 프로그래밍 2

- content pane의 기본 레이아웃은 border layout이다.
- content pane위에 동, 서, 남, 북, 중앙의 위치를 지정해 여러 개의 component를 올릴 수 있다.
- 텍스트 상자의 텍스트를 가져오는 메소드는 getText()이다.
- 라벨에 쓰여진 텍스트를 지정하는 메소드는 setText()이다.
- content pane에서 자주 사용되는 레이아웃에는 grid, flow, box layout이 있다.
- 패널을 이용해 복합 레이아웃을 구성할 수 있다.

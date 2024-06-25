// Generated from /home/felix/Documents/sync/Uni/SS24/COMP/gba/main/Compiler/Slang.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SlangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, INT=8, IDENT=9, 
		COMM=10, NEWLINE=11, WS=12;
	public static final int
		RULE_start = 0, RULE_prog = 1, RULE_line = 2, RULE_expression = 3, RULE_brackets = 4, 
		RULE_assignment = 5, RULE_addition = 6, RULE_subtraction = 7, RULE_multiplication = 8, 
		RULE_division = 9, RULE_value = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "prog", "line", "expression", "brackets", "assignment", "addition", 
			"subtraction", "multiplication", "division", "value"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'='", "'+'", "'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "INT", "IDENT", "COMM", 
			"NEWLINE", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Slang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SlangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class StartContext extends ParserRuleContext {
		public ProgContext prog() {
			return getRuleContext(ProgContext.class,0);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			prog();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ProgContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(SlangParser.EOF, 0); }
		public List<LineContext> line() {
			return getRuleContexts(LineContext.class);
		}
		public LineContext line(int i) {
			return getRuleContext(LineContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(SlangParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(SlangParser.NEWLINE, i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_prog);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(29);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(24);
					line();
					setState(25);
					match(NEWLINE);
					}
					} 
				}
				setState(31);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			}
			setState(33);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENT || _la==COMM) {
				{
				setState(32);
				line();
				}
			}

			setState(35);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LineContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public TerminalNode WS() { return getToken(SlangParser.WS, 0); }
		public TerminalNode COMM() { return getToken(SlangParser.COMM, 0); }
		public LineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_line; }
	}

	public final LineContext line() throws RecognitionException {
		LineContext _localctx = new LineContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_line);
		int _la;
		try {
			setState(45);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENT:
				enterOuterAlt(_localctx, 1);
				{
				setState(37);
				assignment();
				setState(39);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(38);
					match(WS);
					}
				}

				setState(42);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMM) {
					{
					setState(41);
					match(COMM);
					}
				}

				}
				break;
			case COMM:
				enterOuterAlt(_localctx, 2);
				{
				setState(44);
				match(COMM);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public AdditionContext addition() {
			return getRuleContext(AdditionContext.class,0);
		}
		public SubtractionContext subtraction() {
			return getRuleContext(SubtractionContext.class,0);
		}
		public MultiplicationContext multiplication() {
			return getRuleContext(MultiplicationContext.class,0);
		}
		public DivisionContext division() {
			return getRuleContext(DivisionContext.class,0);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_expression);
		try {
			setState(53);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(48);
				addition();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(49);
				subtraction();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(50);
				multiplication();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(51);
				division();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(52);
				value();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BracketsContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> WS() { return getTokens(SlangParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(SlangParser.WS, i);
		}
		public BracketsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_brackets; }
	}

	public final BracketsContext brackets() throws RecognitionException {
		BracketsContext _localctx = new BracketsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_brackets);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			match(T__0);
			setState(57);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(56);
				match(WS);
				}
				break;
			}
			setState(59);
			expression();
			setState(61);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(60);
				match(WS);
				}
			}

			setState(63);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(SlangParser.IDENT, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> WS() { return getTokens(SlangParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(SlangParser.WS, i);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(65);
			match(IDENT);
			setState(67);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(66);
				match(WS);
				}
			}

			setState(69);
			match(T__2);
			setState(71);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(70);
				match(WS);
				}
				break;
			}
			setState(73);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AdditionContext extends ParserRuleContext {
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public List<TerminalNode> WS() { return getTokens(SlangParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(SlangParser.WS, i);
		}
		public AdditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_addition; }
	}

	public final AdditionContext addition() throws RecognitionException {
		AdditionContext _localctx = new AdditionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_addition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			value();
			setState(77);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(76);
				match(WS);
				}
			}

			setState(79);
			match(T__3);
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(80);
				match(WS);
				}
			}

			setState(83);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubtractionContext extends ParserRuleContext {
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public List<TerminalNode> WS() { return getTokens(SlangParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(SlangParser.WS, i);
		}
		public SubtractionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subtraction; }
	}

	public final SubtractionContext subtraction() throws RecognitionException {
		SubtractionContext _localctx = new SubtractionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_subtraction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			value();
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(86);
				match(WS);
				}
			}

			setState(89);
			match(T__4);
			setState(91);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(90);
				match(WS);
				}
			}

			setState(93);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MultiplicationContext extends ParserRuleContext {
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public List<TerminalNode> WS() { return getTokens(SlangParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(SlangParser.WS, i);
		}
		public MultiplicationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplication; }
	}

	public final MultiplicationContext multiplication() throws RecognitionException {
		MultiplicationContext _localctx = new MultiplicationContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_multiplication);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			value();
			setState(97);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(96);
				match(WS);
				}
			}

			setState(99);
			match(T__5);
			setState(101);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(100);
				match(WS);
				}
			}

			setState(103);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DivisionContext extends ParserRuleContext {
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public List<TerminalNode> WS() { return getTokens(SlangParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(SlangParser.WS, i);
		}
		public DivisionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_division; }
	}

	public final DivisionContext division() throws RecognitionException {
		DivisionContext _localctx = new DivisionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_division);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			value();
			setState(107);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(106);
				match(WS);
				}
			}

			setState(109);
			match(T__6);
			setState(111);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WS) {
				{
				setState(110);
				match(WS);
				}
			}

			setState(113);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ValueContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(SlangParser.IDENT, 0); }
		public TerminalNode INT() { return getToken(SlangParser.INT, 0); }
		public BracketsContext brackets() {
			return getRuleContext(BracketsContext.class,0);
		}
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_value);
		try {
			setState(118);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENT:
				enterOuterAlt(_localctx, 1);
				{
				setState(115);
				match(IDENT);
				}
				break;
			case INT:
				enterOuterAlt(_localctx, 2);
				{
				setState(116);
				match(INT);
				}
				break;
			case T__0:
				enterOuterAlt(_localctx, 3);
				{
				setState(117);
				brackets();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16{\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\3\2\3\2\3\3\3\3\3\3\7\3\36\n\3\f\3\16\3!\13\3\3\3\5\3$\n\3\3\3"+
		"\3\3\3\4\3\4\5\4*\n\4\3\4\5\4-\n\4\3\4\5\4\60\n\4\3\5\3\5\3\5\3\5\3\5"+
		"\3\5\5\58\n\5\3\6\3\6\5\6<\n\6\3\6\3\6\5\6@\n\6\3\6\3\6\3\7\3\7\5\7F\n"+
		"\7\3\7\3\7\5\7J\n\7\3\7\3\7\3\b\3\b\5\bP\n\b\3\b\3\b\5\bT\n\b\3\b\3\b"+
		"\3\t\3\t\5\tZ\n\t\3\t\3\t\5\t^\n\t\3\t\3\t\3\n\3\n\5\nd\n\n\3\n\3\n\5"+
		"\nh\n\n\3\n\3\n\3\13\3\13\5\13n\n\13\3\13\3\13\5\13r\n\13\3\13\3\13\3"+
		"\f\3\f\3\f\5\fy\n\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24\26\2\2\2\u0087\2"+
		"\30\3\2\2\2\4\37\3\2\2\2\6/\3\2\2\2\b\67\3\2\2\2\n9\3\2\2\2\fC\3\2\2\2"+
		"\16M\3\2\2\2\20W\3\2\2\2\22a\3\2\2\2\24k\3\2\2\2\26x\3\2\2\2\30\31\5\4"+
		"\3\2\31\3\3\2\2\2\32\33\5\6\4\2\33\34\7\r\2\2\34\36\3\2\2\2\35\32\3\2"+
		"\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 #\3\2\2\2!\37\3\2\2\2\"$\5"+
		"\6\4\2#\"\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&\7\2\2\3&\5\3\2\2\2\')\5\f\7\2"+
		"(*\7\16\2\2)(\3\2\2\2)*\3\2\2\2*,\3\2\2\2+-\7\f\2\2,+\3\2\2\2,-\3\2\2"+
		"\2-\60\3\2\2\2.\60\7\f\2\2/\'\3\2\2\2/.\3\2\2\2\60\7\3\2\2\2\618\3\2\2"+
		"\2\628\5\16\b\2\638\5\20\t\2\648\5\22\n\2\658\5\24\13\2\668\5\26\f\2\67"+
		"\61\3\2\2\2\67\62\3\2\2\2\67\63\3\2\2\2\67\64\3\2\2\2\67\65\3\2\2\2\67"+
		"\66\3\2\2\28\t\3\2\2\29;\7\3\2\2:<\7\16\2\2;:\3\2\2\2;<\3\2\2\2<=\3\2"+
		"\2\2=?\5\b\5\2>@\7\16\2\2?>\3\2\2\2?@\3\2\2\2@A\3\2\2\2AB\7\4\2\2B\13"+
		"\3\2\2\2CE\7\13\2\2DF\7\16\2\2ED\3\2\2\2EF\3\2\2\2FG\3\2\2\2GI\7\5\2\2"+
		"HJ\7\16\2\2IH\3\2\2\2IJ\3\2\2\2JK\3\2\2\2KL\5\b\5\2L\r\3\2\2\2MO\5\26"+
		"\f\2NP\7\16\2\2ON\3\2\2\2OP\3\2\2\2PQ\3\2\2\2QS\7\6\2\2RT\7\16\2\2SR\3"+
		"\2\2\2ST\3\2\2\2TU\3\2\2\2UV\5\26\f\2V\17\3\2\2\2WY\5\26\f\2XZ\7\16\2"+
		"\2YX\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[]\7\7\2\2\\^\7\16\2\2]\\\3\2\2\2]^\3"+
		"\2\2\2^_\3\2\2\2_`\5\26\f\2`\21\3\2\2\2ac\5\26\f\2bd\7\16\2\2cb\3\2\2"+
		"\2cd\3\2\2\2de\3\2\2\2eg\7\b\2\2fh\7\16\2\2gf\3\2\2\2gh\3\2\2\2hi\3\2"+
		"\2\2ij\5\26\f\2j\23\3\2\2\2km\5\26\f\2ln\7\16\2\2ml\3\2\2\2mn\3\2\2\2"+
		"no\3\2\2\2oq\7\t\2\2pr\7\16\2\2qp\3\2\2\2qr\3\2\2\2rs\3\2\2\2st\5\26\f"+
		"\2t\25\3\2\2\2uy\7\13\2\2vy\7\n\2\2wy\5\n\6\2xu\3\2\2\2xv\3\2\2\2xw\3"+
		"\2\2\2y\27\3\2\2\2\25\37#),/\67;?EIOSY]cgmqx";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}